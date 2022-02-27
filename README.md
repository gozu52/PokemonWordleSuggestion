# PokemonWordleSuggestion
Explanation:
This is an application that guesses the answer to pokemonWordle based on the entered Pokemon name, green location, and yellow location.

ver 4 (2022/02/28) 
Change function 
・Support for full-width characters 
・Support for special characters ,the sonant mark (dakuten), P-sound consonant mark (handakuten), geminate consonant (sokuon) and contracted sound (youon) 
・From all suggestions, weight the list of suggestions and suggest the top five 

ver 3 (2022/02/26)
Addition one function
・first suggestion list

ver 2 (2022/02/25)
Addition of the following functions.
・Add accumulation function
・Removed Pokémon from the suggestion list that contain words that don't apply to them
・Changed yellow and green lists from branches to logical conjunction

ver 1 (2022/02/24)
From the Pokemon name you entered, it will derive the next candidate Pokemon name to be entered.
It is not able to determine the sonant mark (dakuten), P-sound consonant mark (handakuten), geminate consonant (sokuon), contracted sound (youon) , and special symbols word, so the answer may not exist among the candidates.
This service need to be activated independently one at a time for now.
