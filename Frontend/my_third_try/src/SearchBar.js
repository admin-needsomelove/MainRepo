import * as React from 'react';
import { Searchbar } from 'react-native-paper';
import { Button } from 'react-native-paper';

const SearchComponent = ( props ) => {
  const [searchQuery, setSearchQuery] = React.useState('');

  const onChangeSearch = query => setSearchQuery(query);

  function handleClick() {
    console.log('Pressed')
    props.navigation.navigate('Results')
  }

  return (
    <div>
      <Searchbar
      placeholder="Search"
      onChangeText={onChangeSearch}
      value={searchQuery}
      />
      <Button mode="contained" onPress={handleClick}> Search </Button>
    </div>
  );
};

export default SearchComponent;