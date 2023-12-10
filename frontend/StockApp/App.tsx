import React, { useState } from 'react';
import { TextInput, Button, Text, View } from 'react-native';
import axios from 'axios';
axios.defaults.withCredentials = false;
axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

const App = () => {
  const [numberInput, setNumberInput] = useState('');
  const [result, setResult] = useState(null);
  const handleNumberChange = (text: string) => setNumberInput(text);
  const url = 'http://127.0.0.1:8000/api/multiply';
  const handleSubmit = async () => {
    const url = `http://127.0.0.1:8000/api/multiply/${numberInput}`;
    try {
      // let n=numberInput.toString()
      console.log(`this is something ${numberInput}`)
      console.log(typeof(numberInput))
      const response = await fetch(`http://127.0.0.1:8000/api/multiply/${numberInput}`);
      console.log("till here")
      // setResult(response.data);
      const data=await response.json()
      setResult(data)
    } catch (error) {
      console.log("i am hehe");
      console.error(error);
    }
  };

  return (
    <View style={{ padding: 20 }}>
      <Text>Enter a number:</Text>
      <TextInput
        value={numberInput}
        onChangeText={handleNumberChange}
        keyboardType="numeric"
      />
      <Button title="Multiply by 10" onPress={handleSubmit} />
      {result !== null && (
        <Text>Result: {numberInput} * 10 = {result}</Text>
      )}
    </View>
  );
};

export default App;
