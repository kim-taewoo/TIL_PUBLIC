import * as firebase from 'firebase/app';
import 'firebase/firestore';

const firebaseConfig = {
  apiKey: 'AIzaSyComB9FqdUr5qUafd8fBP1EegAhiBenEpo',
  authDomain: 'reactonfireudemy.firebaseapp.com',
  databaseURL: 'https://reactonfireudemy.firebaseio.com',
  projectId: 'reactonfireudemy',
  storageBucket: 'reactonfireudemy.appspot.com',
  messagingSenderId: '182078984649',
  appId: '1:182078984649:web:4da7263d4270562b8f9818',
};

firebase.initializeApp(firebaseConfig);

export const db = firebase.firestore();

export default firebase;