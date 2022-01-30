import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import { Button } from 'react-native-paper';
import axios from 'axios';
import { backendParser } from '../services/parser';
import { BACKEND_URL, UPDATE_CUSTOMER_TYPE_PATH } from '../constants/URL';
import { styles } from '../styles/common';


export default function AskingCustomerType ({ route , navigation } ) {

    const [errorMessage, setErrorMessage] = React.useState("")

    function handlePress(account_type) {

        console.log('Customer Type Button Pressed with token '+ global.token)

        const url = BACKEND_URL + UPDATE_CUSTOMER_TYPE_PATH;
        const request_data = {
          token: global.token,
          account_type: account_type
        }
        axios.post(url, request_data)
          .then(function (response) {
            console.log(backendParser(response));
            if (response.data && response.data.hasOwnProperty('Exception')){
              handleExceptions(response)
            }
            else {
              //navigate to next component
            }
          })
          .catch(function (error) {
            console.log(error);
          });
    }

    function handleExceptions(response){
      const exceptionName = response.data['Exception']
      setErrorMessage(exceptionName)
    }

    return (
        <View style={styles.container}>
          <Text style={styles.red}>{errorMessage}</Text>
          <Text>Choose who you are bitch</Text>
          <Button title="Friendster" mode="contained" onPress={() => handlePress('Friendster')}>Friendster</Button>
          <Button title="Seeker" mode="contained" onPress={() => handlePress('Seeker')}>Seeker</Button>
        </View>
      )

}
