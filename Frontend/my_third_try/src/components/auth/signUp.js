import * as React from 'react';
import { TextInput, Button, Text } from 'react-native-paper';
import { View } from 'react-native';
import { styles } from '../../styles/common';
import axios from 'axios';
import { BACKEND_URL, SIGNUP_PATH } from '../../constants/URL';
import { backendParser } from '../../services/parser';

export default function Signup ({ route , navigation } ) {

      const [username, setUsername] = React.useState("");
      const [password, setPassword] = React.useState("");
      const [errorMessage, setErrorMessage] = React.useState("");

      function onCreateAccount() {
        console.log('Create Account Pressed')

        const url = BACKEND_URL + SIGNUP_PATH;
        axios.post(url, {
            username: username,
            password: password
        })
          .then(function (response) {
            console.log(backendParser(response));
            if (response.data['Error']){
              console.log("username exists")
              setErrorMessage("Username already exists")
            }
            else {
              navigation.navigate('Login')
            }
          })
          .catch(function (error) {
            console.log(error);
          });

      }
      
      return (
        <View style={styles.container}>
                <Text style={styles.red}>{errorMessage}</Text>
                <TextInput label="username" value={username} onChangeText={text => setUsername(text)}/>
                <TextInput secureTextEntry={true} label="password" value={password} onChangeText={text => setPassword(text)}/>
                <Button mode="contained" onPress={onCreateAccount}>
                    Create account
                </Button>
                <Text>
                    <Text>Already have an account? </Text>
                    <Text onPress={(e) => navigation.navigate('Login')} style={styles.green}>{'Login'}</Text>
                </Text>
                
        </View>
        );
    }