import React, { Component } from 'react';
import { View, Text } from 'react-native';
import { Button } from 'react-native-paper';
import axios from 'axios';
import { Auth } from 'aws-amplify';
import { getGirlsParser } from './services/parser';


export default function Results ({ route , navigation } ) {

    const { searchQuery } = route.params;
    console.log("result got " + searchQuery)

    
    function getBackendData() {

        const url = 'https://lp65hh01w0.execute-api.us-east-1.amazonaws.com/prod/girls';
        axios.post(url, {
            taskType:'getGirls',
            id:'83857'
        })
          .then(function (response) {
            console.log(getGirlsParser(response));
          })
          .catch(function (error) {
            console.log(error);
          });

          Auth.currentUserInfo().then((user) => {
            console.log('user is ' + JSON.stringify(user.username));
          });

          

        
    }

    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Text>Results Screen {getBackendData()}</Text>
        <Button title="Go to Home" mode="contained" onPress={() => navigation.navigate('Home')}>Home</Button>
        <Button title="Go back" mode="contained" onPress={() => navigation.goBack()}>Back</Button>
      </View>
    )
}