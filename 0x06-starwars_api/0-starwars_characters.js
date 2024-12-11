#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie
 * Usage: ./0-starwars_characters.js <Movie ID>
 */

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error("Usage: ./0-starwars_characters.js <Movie ID>");
  process.exit(1);
}

// Base URL for the Star Wars API
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Make a GET request to the API to fetch the movie details
request(apiUrl, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
	}

	if (res.statusCode !== 200) {
		console.error(`Error: Unable to fetch data for movie ID ${movieId}.`);
		return;
	}

	// Parse the response body to JSON
	const movieData = JSON.parse(body);

	// Retrieve the list of character URLs
	const characters = movieData.characters;

	// Fetch and print each character name in the order provided
	fetchCharactersInOrder(characters, 0);
});

/**
 * Recursively fetches and prints character names in order
 * @param {string[]} characters - Array of character URLs
 * @param {number} index - Current index of the character being fetched
 */
function fetchCharactersInOrder(characters, index) {
	if (index >= characters.length) {
		return;
	}

	request(characters[index], (err, res, body) => {
		if (err) {
			console.error(err);
			return;
		}

		if (res.statusCode !== 200) {
			console.error(`Error: Unable to fetch data for character ${index + 1}.`);
			return;
		}

		// Parse the character data and print the name
		const characterData = JSON.parse(body);
		console.log(characterData.name);

		// Recursively fetch the next character
		fetchCharactersInOrder(characters, index + 1);
	});
}
