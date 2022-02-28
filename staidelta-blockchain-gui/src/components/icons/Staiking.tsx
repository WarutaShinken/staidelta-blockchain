import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as StaikingIcon } from './images/staiking.svg';

export default function Staiking(props: SvgIconProps) {
  return <SvgIcon component={StaikingIcon} viewBox="0 0 40 39" {...props} />;
}
