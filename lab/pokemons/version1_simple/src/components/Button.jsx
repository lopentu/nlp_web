export default function Button ({
  onClick, 
  label,
  ...otherProps
}) {
  return (
    <button 
      onClick={onClick} 
      {...otherProps}
    >
      {label}
    </button>
  )
}