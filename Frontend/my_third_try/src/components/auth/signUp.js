import * as React from 'react';
import { TextInput, Button, Text } from 'react-native-paper';

export default function Signup ({ route , navigation } ) {

      const [username, setUsername] = React.useState("");
      const [password, setPassword] = React.useState("");
      
      return (
            <div>
                <TextInput label="username" value={username} onChangeText={text => setUsername(text)}/>
                <TextInput secureTextEntry={true} label="password" value={password} onChangeText={text => setPassword(text)}/>
                <Button mode="contained" onPress={() => console.log('Pressed')}>
                    Create account
                </Button>
                <Text>
                    <Text>Already have an account? </Text>
                    <Text onPress={(e) => navigation.navigate('Login')}>{'Login'}</Text>
                </Text>
                
            </div>
        );
    }