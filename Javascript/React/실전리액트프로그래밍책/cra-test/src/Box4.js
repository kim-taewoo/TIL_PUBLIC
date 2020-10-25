import React from 'react';
import styled from 'styled-components';

const BoxCommon = styled.div`
  height: 50px;
  width: ${props => (props.isBig? 200: 100)}px;
  background-color: #aaaaaa;
`;

export default function Box({ size }) {
  const isBig = size === 'big';
  const label = isBig ? '큰 박스' : '작은 박스';
  return <BoxCommon isBig={isBig}>{label}</BoxCommon>
}

