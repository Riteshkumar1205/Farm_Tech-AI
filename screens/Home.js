import React from 'react';
import { View, Button } from 'react-native';

export default function Home({ navigation }) {
  return (
    <View>
      <Button title="Upload Leaf" onPress={() => navigation.navigate("UploadLeaf")} />
      <Button title="Seed Advisory" onPress={() => navigation.navigate("SeedAdvisory")} />
    </View>
  );
}
