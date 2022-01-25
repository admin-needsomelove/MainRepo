import * as React from 'react';
import { TextInput, Button, Text } from 'react-native-paper';
import { View } from 'react-native';
import { styles } from '../../styles/common';

export default function Login ({ route , navigation } ) {

      const [username, setUsername] = React.useState("");
      const [password, setPassword] = React.useState("");
      
      return (
            <View style={styles.container}>
                <TextInput label="username" value={username} onChangeText={text => setUsername(text)}/>
                <TextInput secureTextEntry={true} label="password" value={password} onChangeText={text => setPassword(text)}/>
                <Button mode="contained" onPress={() => console.log('Pressed')}>
                    Login
                </Button>
                <Text>
                    <Text>Don't have an account? </Text>
                    <Text onPress={(e) => navigation.navigate('SignUp')} style={styles.green}>{'Register'}</Text>
                </Text>
            </View>
        );
    }