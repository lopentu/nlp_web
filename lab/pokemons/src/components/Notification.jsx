import styled from 'styled-components';

const Alert = styled.div`
  margin: 10px; 
  padding: 8px;
  color: white;
  border-radius: 5px;
  background-color: purple;
`;

export default function Notification({
  notification, 
}) {
  return (
      <Alert>
        <p>{notification.count} {notification.pokemonName} has been added to cart!</p>
      </Alert>
    )
}