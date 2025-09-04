import React from 'react';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Home from './screens/Home';
import UploadLeaf from './screens/UploadLeaf';
import SeedAdvisory from './screens/SeedAdvisory';

const Stack = createStackNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen name="Home" component={Home} />
        <Stack.Screen name="UploadLeaf" component={UploadLeaf} />
        <Stack.Screen name="SeedAdvisory" component={SeedAdvisory} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
