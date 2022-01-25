import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import { Button } from 'react-native-paper';
import axios from 'axios';
import { backendParser } from '../services/parser';
import { BACKEND_URL } from '../constants/URL';


export default function Results ({ route , navigation } ) {

    const { searchQuery } = route.params;

    const [ backendData, setBackendData ] = useState(0);

    console.log("profile list is " + searchQuery)

    useEffect(() => {
      const url = BACKEND_URL + 'profileList';
        axios.post(url, {
        })
          .then(function (response) {
            setBackendData(backendParser(response));
          })
          .catch(function (error) {
            console.log(error);
          });
    });

    
    function getBackendData() {

        const url = 'https://4rhtw1mjta.execute-api.us-east-1.amazonaws.com/prod/profileList';
        axios.post(url, {
        })
          .then(function (response) {
            setBackendData(response);
          })
          .catch(function (error) {
            console.log(error);
          });
    }

    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Text>Results Screen</Text>
        <Text>{ backendData }</Text>
        <Button title="Go to Home" mode="contained" onPress={() => navigation.navigate('Home')}>Home</Button>
        <Button title="Go back" mode="contained" onPress={() => navigation.goBack()}>Back</Button>
      </View>
    )
}