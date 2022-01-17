import React, { Component } from 'react';
import { View, Text } from 'react-native';
import { Button } from 'react-native-paper';

export default function Results ({ navigation } ) {
    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
        <Text>Results Screen</Text>
        <Button title="Go to Home" mode="contained" onPress={() => navigation.navigate('Home')}>Home</Button>
        <Button title="Go back" mode="contained" onPress={() => navigation.goBack()}>Back</Button>
      </View>
    )
}