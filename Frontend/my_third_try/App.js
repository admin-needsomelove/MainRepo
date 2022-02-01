import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import SearchComponent  from './src/components/SearchBar'
import Results from './src/components/Results'
import Welcome from './src/components/Welcome'
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import SignUp from './src/components/auth/signUp'
import Login from './src/components/auth/login';
import AskingCustomerType from './src/components/AskingCustomerType';
import Chat from './src/components/chat/Chat';
import FileSelector from './src/components/UploadImages';

import store from './src/services/reduxStore'
import { Provider } from 'react-redux'


function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text>Open up App.js to start working on your app! </Text>
      <SearchComponent navigation={ navigation }></SearchComponent>
      <StatusBar style="auto" />
    </View>
  );
}

const Stack = createNativeStackNavigator();

function App() {
  return (
    <Provider store={store}>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="SignUp">
          <Stack.Screen name="Home" component={HomeScreen} />
          <Stack.Screen name="SignUp" component={SignUp} />
          <Stack.Screen name="Login" component={Login} />
          <Stack.Screen name="AskingCustomerType" component={AskingCustomerType} />
          <Stack.Screen name="Welcome" component={Welcome} />
          <Stack.Screen name="Results" component={Results} />
          <Stack.Screen name="Chat" component={Chat} />
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>
    
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default App;
