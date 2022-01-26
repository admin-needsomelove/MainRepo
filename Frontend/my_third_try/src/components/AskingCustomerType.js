import React, { useState, useEffect } from 'react';
import { View, Text } from 'react-native';
import { Button } from 'react-native-paper';
import axios from 'axios';
import { backendParser } from '../services/parser';
import { BACKEND_URL, UPDATE_CUSTOMER_TYPE_PATH } from '../constants/URL';
import { styles } from '../styles/common';


export default function AskingCustomerType ({ route , navigation } ) {

    function onButtonPress(customer_type) {

        console.log('Customer Type Button Pressed with token '+ global.token)

        const url = BACKEND_URL + UPDATE_CUSTOMER_TYPE_PATH;
        axios.post(url, {
            token: global.token,
            customer_type: customer_type
        })
          .then(function (response) {
            console.log(backendParser(response));
          })
          .catch(function (error) {
            console.log(error);
          });
    }

    return (
        <View style={styles.container}>
          <Text>Choose who you are bitch</Text>
          <Button title="Friendster" mode="contained" onPress={onButtonPress('Friendster')}>Friendster</Button>
          <Button title="Seeker" mode="contained" onPress={onButtonPress('Seeker')}>Seeker</Button>
        </View>
      )

}
