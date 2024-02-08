const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const dbPath = path.resolve(__dirname, 'venues.db');
const db = new sqlite3.Database(dbPath);


db.serialize(() => {
  // Create the "venues" table
  db.run(`
    CREATE TABLE IF NOT EXISTS venues (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      location TEXT NOT NULL,
      city TEXT NOT NULL,
      count INTEGER NOT NULL
    )
  `, (err) => {
    if (err) {
      console.error('Error creating venues table:', err);
    }
  });

  // Create the "shows" table
  db.run(`
    CREATE TABLE IF NOT EXISTS shows (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      venue_id INTEGER NOT NULL,
      name TEXT NOT NULL,
      rating INTEGER NOT NULL,
      timing TEXT NOT NULL,
      tags TEXT NOT NULL,
      price INTEGER NOT NULL,
      count INTEGER NOT NULL,
      FOREIGN KEY (venue_id) REFERENCES venues(id)
    )
  `, (err) => {
    if (err) {
      console.error('Error creating shows table:', err);
    }
  });
});

module.exports = db;
