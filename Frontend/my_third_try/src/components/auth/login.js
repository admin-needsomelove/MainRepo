import * as React from 'react';
import { TextInput, Button, Text } from 'react-native-paper';

export default function Login ({ route , navigation } ) {

      const [username, setUsername] = React.useState("");
      const [password, setPassword] = React.useState("");
      
      return (
            <div>
                <TextInput label="username" value={username} onChangeText={text => setUsername(text)}/>
                <TextInput secureTextEntry={true} label="password" value={password} onChangeText={text => setPassword(text)}/>
                <Button mode="contained" onPress={() => console.log('Pressed')}>
                    Login
                </Button>
                <Text>
                    <Text>Don't have an account? </Text>
                    <Text onPress={(e) => navigation.navigate('SignUp')}>{'Register'}</Text>
                </Text>
            </div>
        );
    }