import React from 'react';
import styled from 'styled-components';
import { Box, BoxProps } from '@material-ui/core';
import { StaiDelta } from '@staidelta/icons';

const StyledStaiDelta = styled(StaiDelta)`
  max-width: 100%;
  width: auto;
  height: auto;
`;

export default function Logo(props: BoxProps) {
  return (
    <Box {...props}>
      <StyledStaiDelta />
    </Box>
  );
}
