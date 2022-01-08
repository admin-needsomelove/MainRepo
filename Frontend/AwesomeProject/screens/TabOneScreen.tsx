import { useState } from 'react';
import { ScrollView, StyleSheet, TextInput, Image, Button } from 'react-native';

import EditScreenInfo from '../components/EditScreenInfo';
import { Text, View } from '../components/Themed';
import { RootTabScreenProps } from '../types';
import TabTwoScreen from './TabTwoScreen';

export default function TabOneScreen({ navigation }: RootTabScreenProps<'TabOne'>) {
  
  const [currentText, setText] = useState('');

  return (
    <View style={styles.container}>
      <Text style={styles.title}>{currentText}</Text>
      <Text >Hodggi</Text>
      <Button onPress={navigation.navigate('TabTwo')}></Button>
      <Image source={{
        uri: 'https://reactnative.dev/docs/assets/p_cat2.png',
        }} style={{ width: 200, height: 200 }}></Image>
      <TextInput style={{height=40,width=40}} onChangeText={setText}></TextInput>
      <View style={styles.separator} lightColor="#eee" darkColor="rgba(255,255,255,0.1)" />
      <EditScreenInfo path="/screens/TabOneScreen.tsx" />
      
      
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  separator: {
    marginVertical: 30,
    height: 1,
    width: '80%',
  },
});
