import * as React from 'react';
import { TextInput, Button, Text } from 'react-native-paper';
import { View } from 'react-native';
import { styles } from '../../styles/common';
import axios from 'axios';
import { BACKEND_URL, SIGNIN_PATH } from '../../constants/URL';
import { INCORRECT_USERNAME_PASSWORD } from '../../constants/Exceptions';

export default function Login ({ route , navigation } ) {

      const [username, setUsername] = React.useState("");
      const [password, setPassword] = React.useState("");
      const userCreationMessage = 'params' in route ? route.params.userCreationSuccessful : {};
      const [errorMessage, setErrorMessage] = React.useState(userCreationMessage)

      function onLoginPress() {
        console.log('Login Pressed')

        const url = BACKEND_URL + SIGNIN_PATH;
        const request_data = {
            username: username,
            password: password
        }
        axios.post(url, request_data)
          .then(function (response) {
            console.log(response)
            if (response.data.hasOwnProperty('Exception')){
                handleExceptions(response)
            }
            else {
                if (response.data.hasOwnProperty('token')){
                    global.token = response.data.token
                    navigation.navigate('AskingCustomerType')
                }
            }
          })
          .catch(function (error) {
            console.log(error)
            setErrorMessage("Service error. Please try again later");
          });
      }

      function handleExceptions(response){
            const exceptionName = response.data['Exception']
            if (exceptionName==INCORRECT_USERNAME_PASSWORD){
                setErrorMessage("Username or password incorrect");
            }
            else {
                throw exceptionName
            }
        }
      
      
      return (
            <View style={styles.container}>
                <Text style={styles.red}>{errorMessage}</Text>
                <TextInput label="username" value={username} onChangeText={text => setUsername(text)}/>
                <TextInput secureTextEntry={true} label="password" value={password} onChangeText={text => setPassword(text)}/>
                <Button mode="contained" onPress={onLoginPress}>
                    Login
                </Button>
                <Text>
                    <Text>Don't have an account? </Text>
                    <Text onPress={(e) => navigation.navigate('SignUp')} style={styles.green}>{'Register'}</Text>
                </Text>
            </View>
        );
    }