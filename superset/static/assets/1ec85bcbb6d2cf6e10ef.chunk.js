"use strict";(globalThis.webpackChunksuperset=globalThis.webpackChunksuperset||[]).push([[704],{33738:(e,t,r)=>{r.r(t),r.d(t,{default:()=>d});var l=r(67294),a=r(16355),n=r(5364),s=r(51115),u=r(67190),i=r(10581),c=r(63475),o=r(6915),h=r(11965);function d(e){let{height:t,width:r,echartOptions:d,setDataMask:p,labelMap:f,labelMapB:g,groupby:m,groupbyB:b,selectedValues:v,formData:y,emitCrossFilters:w,seriesBreakdown:k,onContextMenu:F,onFocusedSeries:x,xValueFormatter:E,xAxis:C,refs:V,coltypeMapping:I}=e;const M=(0,l.useCallback)((e=>e<k),[k]),N=(0,l.useCallback)(((e,t)=>{const r=Object.values(v||{});let l;l=r.includes(e)?r.filter((t=>t!==e)):[e];const a=M(t)?m:b,n=M(t)?f:g,s=l.map((e=>null==n?void 0:n[e])).filter((e=>!!e));return{dataMask:{extraFormData:{filters:0===l.length?[]:[...a.map(((e,t)=>{const r=s.map((e=>e[t]));return null==r?{col:e,op:"IS NULL"}:{col:e,op:"IN",val:r}}))]},filterState:{value:s.length?s:null,selectedValues:l.length?l:null}},isCurrentValueSelected:r.includes(e)}}),[m,b,M,f,g,v]),O=(0,l.useCallback)(((e,t)=>{w&&p(N(e,t).dataMask)}),[w,p,N]),S={click:e=>{const{seriesName:t,seriesIndex:r}=e;O(t,r)},mouseout:()=>{x(null)},mouseover:e=>{x(e.seriesName)},contextmenu:async e=>{if(F){e.event.stop();const{data:t,seriesName:r,seriesIndex:l}=e,c=e.event.event,h=[],d=[],p=M(l),m=[...e.name?[e.name]:[],...(p?f:g)[e.seriesName]];t&&C.type===a.we.time&&h.push({col:C.label===n.W3?y.granularitySqla:C.label,grain:y.timeGrainSqla,op:"==",val:t[0],formattedVal:E(t[0])}),[...t&&C.type===a.we.category?[C.label]:[],...p?y.groupby:y.groupbyB].forEach(((e,t)=>h.push({col:e,op:"==",val:m[t],formattedVal:String(m[t])}))),[...p?y.groupby:y.groupbyB].forEach(((e,t)=>d.push({col:e,op:"==",val:m[t],formattedVal:(0,o.mj)(m[t],{timeFormatter:(0,s.bt)(y.dateFormat),numberFormatter:(0,u.JB)(y.numberFormat),coltype:null==I?void 0:I[(0,i.Z)(e)]})}))),F(c.clientX,c.clientY,{drillToDetail:h,crossFilter:N(r,l),drillBy:{filters:d,groupbyFieldName:p?"groupby":"groupby_b",adhocFilterFieldName:p?"adhoc_filters":"adhoc_filters_b"}})}}};return(0,h.tZ)(c.Z,{refs:V,height:t,width:r,echartOptions:d,eventHandlers:S,selectedValues:v})}},63475:(e,t,r)=>{r.d(t,{Z:()=>c});var l=r(67294),a=r(51995),n=r(31431),s=r(11965);const u=a.iK.div`
  height: ${e=>{let{height:t}=e;return t}};
  width: ${e=>{let{width:t}=e;return t}};
`;function i(e,t){let{width:r,height:a,echartOptions:i,eventHandlers:c,zrEventHandlers:o,selectedValues:h={},refs:d}=e;const p=(0,l.useRef)(null);d&&(d.divRef=p);const f=(0,l.useRef)(),g=(0,l.useMemo)((()=>Object.keys(h)||[]),[h]),m=(0,l.useRef)([]);(0,l.useImperativeHandle)(t,(()=>({getEchartInstance:()=>f.current}))),(0,l.useEffect)((()=>{p.current&&(f.current||(f.current=(0,n.S1)(p.current)),Object.entries(c||{}).forEach((e=>{var t,r;let[l,a]=e;null==(t=f.current)||t.off(l),null==(r=f.current)||r.on(l,a)})),Object.entries(o||{}).forEach((e=>{var t,r;let[l,a]=e;null==(t=f.current)||t.getZr().off(l),null==(r=f.current)||r.getZr().on(l,a)})),f.current.setOption(i,!0))}),[i,c,o]),(0,l.useEffect)((()=>{f.current&&(f.current.dispatchAction({type:"downplay",dataIndex:m.current.filter((e=>!g.includes(e)))}),g.length&&f.current.dispatchAction({type:"highlight",dataIndex:g}),m.current=g)}),[g]);const b=(0,l.useCallback)((e=>{let{width:t,height:r}=e;f.current&&f.current.resize({width:t,height:r})}),[]);return(0,l.useEffect)((()=>(b({width:r,height:a}),()=>{var e;return null==(e=f.current)?void 0:e.dispose()})),[]),(0,l.useLayoutEffect)((()=>{b({width:r,height:a})}),[r,a,b]),(0,s.tZ)(u,{ref:p,height:a,width:r})}const c=(0,l.forwardRef)(i)}}]);
//# sourceMappingURL=1ec85bcbb6d2cf6e10ef.chunk.js.map