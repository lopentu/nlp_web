export default function CartItem({pokemon}){
  return (
    <div key={`${pokemon.id}_${pokemon.name}`}>
      <p>
        <span>{pokemon.name}{' '}</span>
        <span>count: {pokemon.count}</span>
      </p>
      <p>subtotal: ${pokemon.count * pokemon.price}</p>
      <hr />
    </div>
  )
}