/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import {
  CSSProperties,
  ReactNode,
  useCallback,
  useEffect,
  useMemo,
  useRef,
  useState,
} from 'react';
import { Menu } from '@superset-ui/core/components/Menu';
import {
  BaseFormData,
  Behavior,
  Column,
  ContextMenuFilters,
  JsonResponse,
  css,
  ensureIsArray,
  getChartMetadataRegistry,
  getExtensionsRegistry,
  logging,
  t,
  useTheme,
} from '@superset-ui/core';
import { Constants, Input, Loading } from '@superset-ui/core/components';
import rison from 'rison';
import { debounce } from 'lodash';
import { FixedSizeList as List } from 'react-window';
import { Icons } from '@superset-ui/core/components/Icons';
import { useToasts } from 'src/components/MessageToasts/withToasts';
import {
  cachedSupersetGet,
  supersetGetCache,
} from 'src/utils/cachedSupersetGet';
import { InputRef } from 'antd';
import { MenuItemTooltip } from '../DisabledMenuItemTooltip';
import { getSubmenuYOffset } from '../utils';
import { VirtualizedMenuItem } from '../MenuItemWithTruncation';
import { Dataset } from '../types';

const SUBMENU_HEIGHT = 200;
const SHOW_COLUMNS_SEARCH_THRESHOLD = 10;
const SEARCH_INPUT_HEIGHT = 48;

export interface DrillByMenuItemsProps {
  drillByConfig?: ContextMenuFilters['drillBy'];
  formData: BaseFormData & { [key: string]: any };
  contextMenuY?: number;
  submenuIndex?: number;
  onSelection?: (...args: any) => void;
  onClick?: (event: MouseEvent) => void;
  onCloseMenu?: () => void;
  openNewModal?: boolean;
  excludedColumns?: Column[];
  open: boolean;
  onDrillBy?: (column: Column, dataset: Dataset) => void;
}

const loadDrillByOptions = getExtensionsRegistry().get('load.drillby.options');

const queryString = rison.encode({
  columns: [
    'table_name',
    'owners.first_name',
    'owners.last_name',
    'created_by.first_name',
    'created_by.last_name',
    'created_on_humanized',
    'changed_by.first_name',
    'changed_by.last_name',
    'changed_on_humanized',
    'columns.column_name',
    'columns.verbose_name',
    'columns.groupby',
  ],
});

export const DrillByMenuItems = ({
  drillByConfig,
  formData,
  contextMenuY = 0,
  submenuIndex = 0,
  onSelection = () => {},
  onClick = () => {},
  onCloseMenu = () => {},
  excludedColumns,
  openNewModal = true,
  open,
  onDrillBy,
  ...rest
}: DrillByMenuItemsProps) => {
  const theme = useTheme();
  const { addDangerToast } = useToasts();
  const [isLoadingColumns, setIsLoadingColumns] = useState(true);
  const [searchInput, setSearchInput] = useState('');
  const [debouncedSearchInput, setDebouncedSearchInput] = useState('');
  const [dataset, setDataset] = useState<Dataset>();
  const [columns, setColumns] = useState<Column[]>([]);
  const ref = useRef<InputRef>(null);
  const showSearch =
    loadDrillByOptions || columns.length > SHOW_COLUMNS_SEARCH_THRESHOLD;

  const handleSelection = useCallback(
    (event, column) => {
      onClick(event);
      onSelection(column, drillByConfig);
      if (openNewModal && onDrillBy && dataset) {
        onDrillBy(column, dataset);
      }
      onCloseMenu();
    },
    [drillByConfig, onClick, onSelection, openNewModal, onDrillBy, dataset],
  );

  useEffect(() => {
    if (open) {
      ref.current?.input?.focus({ preventScroll: true });
    } else {
      // Reset search input when menu is closed
      setSearchInput('');
      setDebouncedSearchInput('');
    }
  }, [open]);

  const hasDrillBy = drillByConfig?.groupbyFieldName;

  const handlesDimensionContextMenu = useMemo(
    () =>
      getChartMetadataRegistry()
        .get(formData.viz_type)
        ?.behaviors.find(behavior => behavior === Behavior.DrillBy),
    [formData.viz_type],
  );

  useEffect(() => {
    async function loadOptions() {
      const datasetId = Number(formData.datasource.split('__')[0]);
      try {
        setIsLoadingColumns(true);
        let response: JsonResponse;
        if (loadDrillByOptions) {
          response = await loadDrillByOptions(datasetId, formData);
        } else {
          response = await cachedSupersetGet({
            endpoint: `/api/v1/dataset/${datasetId}?q=${queryString}`,
          });
        }
        const { json } = response;
        const { result } = json;
        setDataset(result);
        setColumns(
          ensureIsArray(result.columns)
            .filter(column => column.groupby)
            .filter(
              column =>
                !ensureIsArray(
                  formData[drillByConfig?.groupbyFieldName ?? ''],
                ).includes(column.column_name) &&
                column.column_name !== formData.x_axis &&
                ensureIsArray(excludedColumns)?.every(
                  excludedCol => excludedCol.column_name !== column.column_name,
                ),
            ),
        );
      } catch (error) {
        logging.error(error);
        supersetGetCache.delete(`/api/v1/dataset/${datasetId}`);
        addDangerToast(t('Failed to load dimensions for drill by'));
      } finally {
        setIsLoadingColumns(false);
      }
    }
    if (handlesDimensionContextMenu && hasDrillBy) {
      loadOptions();
    }
  }, [
    addDangerToast,
    drillByConfig?.groupbyFieldName,
    excludedColumns,
    formData,
    handlesDimensionContextMenu,
    hasDrillBy,
  ]);

  const debouncedSetSearchInput = useMemo(
    () =>
      debounce((value: string) => {
        setDebouncedSearchInput(value);
      }, Constants.FAST_DEBOUNCE),
    [],
  );

  const handleInput = (value: string) => {
    setSearchInput(value);
    debouncedSetSearchInput(value);
  };

  const filteredColumns = useMemo(
    () =>
      columns.filter(column =>
        (column.verbose_name || column.column_name)
          .toLowerCase()
          .includes(debouncedSearchInput.toLowerCase()),
      ),
    [columns, debouncedSearchInput],
  );

  const submenuYOffset = useMemo(
    () =>
      getSubmenuYOffset(
        contextMenuY,
        filteredColumns.length || 1,
        submenuIndex,
        SUBMENU_HEIGHT,
        showSearch ? SEARCH_INPUT_HEIGHT : 0,
      ),
    [contextMenuY, filteredColumns.length, submenuIndex, showSearch],
  );

  let tooltip: ReactNode;

  if (!handlesDimensionContextMenu) {
    tooltip = t('Drill by is not yet supported for this chart type');
  } else if (!hasDrillBy) {
    tooltip = t('Drill by is not available for this data point');
  }

  if (!handlesDimensionContextMenu || !hasDrillBy) {
    return (
      <Menu.Item key="drill-by-disabled" disabled {...rest}>
        <div>
          {t('Drill by')}
          <MenuItemTooltip title={tooltip} />
        </div>
      </Menu.Item>
    );
  }

  const Row = ({
    index,
    data,
    style,
  }: {
    index: number;
    data: { columns: Column[] };
    style: CSSProperties;
  }) => {
    const { columns, ...rest } = data;
    const column = columns[index];
    return (
      <VirtualizedMenuItem
        tooltipText={column.verbose_name || column.column_name}
        onClick={e => handleSelection(e, column)}
        style={style}
        {...rest}
      >
        {column.verbose_name || column.column_name}
      </VirtualizedMenuItem>
    );
  };

  return (
    <>
      <Menu.SubMenu
        key="drill-by-submenu"
        title={t('Drill by')}
        popupClassName="chart-context-submenu"
        popupOffset={[0, submenuYOffset]}
        {...rest}
      >
        <div data-test="drill-by-submenu">
          {showSearch && (
            <Input
              ref={ref}
              prefix={
                <Icons.SearchOutlined
                  iconSize="l"
                  iconColor={theme.colorIcon}
                />
              }
              onChange={e => {
                e.stopPropagation();
                handleInput(e.target.value);
              }}
              placeholder={t('Search columns')}
              onClick={e => {
                // prevent closing menu when clicking on input
                e.nativeEvent.stopImmediatePropagation();
              }}
              allowClear
              css={css`
                width: auto;
                max-width: 100%;
                margin: ${theme.sizeUnit * 2}px ${theme.sizeUnit * 3}px;
                box-shadow: none;
              `}
              value={searchInput}
            />
          )}
          {isLoadingColumns ? (
            <div
              css={css`
                padding: ${theme.sizeUnit * 3}px 0;
              `}
            >
              <Loading position="inline-centered" />
            </div>
          ) : filteredColumns.length ? (
            <List
              width="100%"
              height={SUBMENU_HEIGHT}
              itemSize={35}
              itemCount={filteredColumns.length}
              itemData={{ columns: filteredColumns, ...rest }}
              overscanCount={20}
            >
              {Row}
            </List>
          ) : (
            <Menu.Item disabled key="no-drill-by-columns-found" {...rest}>
              {t('No columns found')}
            </Menu.Item>
          )}
        </div>
      </Menu.SubMenu>
    </>
  );
};
