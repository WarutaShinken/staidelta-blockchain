import React from 'react';
import { SvgIcon, SvgIconProps } from '@material-ui/core';
import { ReactComponent as StaiDeltaIcon } from './images/staidelta.svg';

export default function Keys(props: SvgIconProps) {
  return <SvgIcon component={StaiDeltaIcon} viewBox="0 0 155 60" {...props} />;
}
