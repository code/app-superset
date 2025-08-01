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
import { MouseEventHandler, ReactNode } from 'react';
import { css, useTheme } from '@superset-ui/core';
import { Icons } from '@superset-ui/core/components/Icons';
import { Tooltip } from '../Tooltip';

export interface PopoverSectionProps {
  title: string;
  isSelected?: boolean;
  onSelect?: MouseEventHandler<HTMLDivElement>;
  info?: string;
  children?: ReactNode;
}

export default function PopoverSection({
  title,
  isSelected,
  children,
  onSelect,
  info,
}: PopoverSectionProps) {
  const theme = useTheme();
  return (
    <div
      css={{
        paddingBottom: theme.sizeUnit * 2,
        opacity: isSelected ? 1 : 0.6,
      }}
    >
      <div
        role="button"
        tabIndex={0}
        onClick={onSelect}
        css={css`
          display: flex;
          align-items: center;
          cursor: ${onSelect ? 'pointer' : 'default'};
        `}
      >
        <strong data-test="popover-title">{title}</strong>
        {info && (
          <Tooltip
            title={info}
            css={css`
              margin-left: ${theme.sizeUnit}px;
              margin-right: ${theme.sizeUnit}px;
            `}
          >
            <Icons.InfoCircleOutlined
              role="img"
              iconSize="s"
              iconColor={theme.colors.grayscale.light1}
            />
          </Tooltip>
        )}
        <Icons.CheckOutlined
          iconSize="s"
          role="img"
          iconColor={
            isSelected ? theme.colorPrimary : theme.colors.grayscale.base
          }
        />
      </div>
      <div
        css={css`
          margin-left: ${theme.sizeUnit}px;
          margin-top: ${theme.sizeUnit}px;
        `}
      >
        {children}
      </div>
    </div>
  );
}
