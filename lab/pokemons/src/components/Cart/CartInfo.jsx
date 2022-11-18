import React from 'react';
import styled from 'styled-components';

import CartItem from './CartItem';
import { sumPrices } from '../../utils/sumPrices';

const Cart = styled.div`
  margin: 10px;
  float: right;
`;

export default function CartInfo({cart}) {
  return (
    <Cart>
    <h3>cart</h3>
        {cart.length <= 0 
          ? 'no added pokemon'
          : (
            <>
              {cart.map(pokemon => <CartItem pokemon={pokemon} />)}
              <p style={{fontWeight: 'bold'}}>Total: ${sumPrices({obj: cart, initialValue: 0})}</p>
            </>
          )}
    </Cart>
  )
}