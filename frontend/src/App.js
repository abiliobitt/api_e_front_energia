import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { faker } from '@faker-js/faker';

import './App.css';
import ASide from './components/aside';
import Header from './components/header';
import { useEffect, useState } from 'react';
import { getApiData } from './services';

const data = [
  {
    name: 'Page A',
    uv: 4000,
    pv: 2400,
    amt: 2400,
  },
  {
    name: 'Page B',
    uv: 3000,
    pv: 1398,
    amt: 2210,
  },
  {
    name: 'Page C',
    uv: 2000,
    pv: 9800,
    amt: 2290,
  },
  {
    name: 'Page D',
    uv: 2780,
    pv: 3908,
    amt: 2000,
  },
  {
    name: 'Page E',
    uv: 1890,
    pv: 4800,
    amt: 2181,
  },
  {
    name: 'Page F',
    uv: 2390,
    pv: 3800,
    amt: 2500,
  },
  {
    name: 'Page G',
    uv: 3490,
    pv: 4300,
    amt: 2100,
  },
];
function App() {
  const [apiData, setApiData] = useState()
  useEffect(() => {
    getApiData('potency_by_uf_and_class')
    .then( response => {
      mountData(response.data)
      setApiData(data)
      
    })
    .catch( error => alert(error))
  }, []);

  const mountData = (data) => {
    const array = []

    const toArray = Object.keys(data.SigUF).map((key) => data.SigUF[key]);
    for (let index = 0; index < toArray.length; index++) {
      console.log(toArray[index])
    }
    // return responseFormated;
  }
  return (
    <div className="App">
      <Header highlight="energia" classes="header" >Dados de </Header>
      {/* <ASide classes="aside" /> */}
        <LineChart
          width={500}
          height={300}
          data={apiData}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Line type="monotone" dataKey="pv" stroke="#8884d8" activeDot={{ r: 8 }} />
          <Line type="monotone" dataKey="uv" stroke="#82ca9d" />
        </LineChart>
    </div>
  );
}

export default App;
