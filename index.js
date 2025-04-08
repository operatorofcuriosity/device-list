import admin from './lib/firebase.js';

async function testFirebase() {
  const db = admin.firestore();
  const collections = await db.listCollections();
  console.log('目前有這些 collections:', collections.map(c => c.id));
}

testFirebase();
