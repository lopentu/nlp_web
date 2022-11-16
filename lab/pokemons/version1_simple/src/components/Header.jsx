import styled from 'styled-components';

import Notification from './Notification';

const HeaderWrapper = styled.header`
  position: fixed;
  background-color: white;
  width: 100%; 
  top: 0;
`;

export default function Header({notification}){
  return (
    <HeaderWrapper>
      <h1 style={{textAlign:'center'}}>Buy Pokemons!</h1>
      {notification && (
        <Notification
          notification={notification}
        />
      )}
    </HeaderWrapper>
  )
}