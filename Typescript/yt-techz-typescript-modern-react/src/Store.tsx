import React, { createContext, useReducer } from 'react';
import { IEpisode, IState, IAction } from './Interfaces';

const initialState: IState = {
  episodes: [],
  favourites: [],
};

export const Store = createContext<IState | any>(initialState);

const reducer = (state: IState, action: IAction): IState => {
  switch (action.type) {
    case 'FETCH_DATA':
      return { ...state, episodes: action.payload };
    case 'ADD_FAV':
      return { ...state, favourites: [...state.favourites, action.payload] };
    case 'REMOVE_FAV':
      const newFavList = state.favourites.filter(
        (fav: IEpisode) => fav.id !== action.payload.id
      );
      return { ...state, favourites: newFavList };
    default:
      return state;
  }
};

export function StoreProvider(props: any): JSX.Element {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <Store.Provider value={{ state, dispatch }}>
      {props.children}
    </Store.Provider>
  );
}
