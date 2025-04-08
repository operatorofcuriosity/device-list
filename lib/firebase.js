// lib/firebase.js
import admin from "firebase-admin";
import { readFileSync } from "fs";

const serviceAccountPath = JSON.parse(
  readFileSync(new URL("../secrets/firebase-service-account.json", import.meta.url))
);

if (!admin.apps.length) {
  admin.initializeApp({
    credential: admin.credential.cert(serviceAccountPath),
  });
}

export default admin;
