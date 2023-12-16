// import React, { useState } from 'react';
// import { TextInput, Button, Text, View } from 'react-native';
// import axios from 'axios';
// axios.defaults.withCredentials = false;
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

// const App = () => {
//   const [numberInput, setNumberInput] = useState('');
//   const [result, setResult] = useState(null);
//   const handleNumberChange = (text: string) => setNumberInput(text);
//   const url = 'http://127.0.0.1:8000/api/multiply';
//   const handleSubmit = async () => {
//     const url = `http://127.0.0.1:8000/api/multiply/${numberInput}`;
//     try {
      
//       console.log(`this is something ${numberInput}`)
//       console.log(typeof(numberInput))
//       const response = await axios.get(url);
//       console.log("till here")
//       setResult(response.data.result);
//       console.log(response.data.result);

      
//     } catch (error) {
//       console.log("i am hehe");
//       console.error(error);
//     }
//   };

//   return (
//     <View style={{ padding: 20 }}>
//       <Text>Enter a number:</Text>
//       <TextInput
//         value={numberInput}
//         onChangeText={handleNumberChange}
//         keyboardType="numeric"
//       />
//       <Button title="Multiply by 10" onPress={handleSubmit} />
//       {result !== null && (
//         <Text>Result: {numberInput} * 10 = {result}</Text>
//       )}
//     </View>
//   );
// };

// export default App;
import React, { useState } from 'react';
import axios from 'axios';

interface ApiResponse {
  result: number;
}

function App() {
  const [inputValue, setInputValue] = useState<string>('');
  const [result, setResult] = useState<any | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(e.target.value);
  };

  const fetchData = async () => {
    try {
      const response = await axios.get<ApiResponse>(`http://127.0.0.1:8000/api/multiply/${inputValue}`);
      const resultValue = response.data.result;
      console.log(resultValue)
      setResult(resultValue);
      setError(null);
    } catch (error) {
      setError('An error occurred. Please try again.');
      setResult(null);
    }
  };

  return (
    <div>
      <h1>React Django Example</h1>
      <label>
        Enter a number:
        <input type="number" value={inputValue} onChange={handleInputChange} />
      </label>
      <button onClick={fetchData}>Multiply by 10</button>
      {result !== null && 
      <table> <tbody>
         {/* <td>{result.results[0]}</td> : */}
        <td>{result.results[0].AAEEF}</td>
      </tbody> </table>
      }
      {error && <p>{error}</p>}
    </div>
  );
}

export default App;
