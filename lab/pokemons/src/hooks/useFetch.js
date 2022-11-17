import { useState , useEffect} from 'react';

const useFetch = ({url, resolvedPath}) => {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch(url)
      .then(response => {
        console.log(response);
        return response.json();
      })
      .then(data => {
        setData(resolvedPath ? data[resolvedPath] : data);
      })
      .catch(error=> setError(error))
      .finally(()=> setLoading(false))
  }, [resolvedPath, url])

  return {
    loading, 
    error,
    data
  }
}

export default useFetch;