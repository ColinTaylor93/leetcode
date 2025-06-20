class Codec:
    def __init__(self):
        # Maps original long URLs to their generated short codes
        self.long_to_short_map = {}

        # Maps generated short codes back to original long URLs
        self.short_to_long_map = {}

    def encode(self, longUrl: str) -> str:
        """
        Encodes a URL to a shortened URL.
        """
        character_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        base_url = "http://tinyurl.com/"

        # Only generate a new code if the URL hasn't been encoded yet
        while longUrl not in self.long_to_short_map:
            # Generate a random 6-character code
            short_code = ''.join(random.choice(character_set) for _ in range(6))

            # Ensure the code hasn't been used yet
            if short_code not in self.short_to_long_map:
                self.short_to_long_map[short_code] = longUrl
                self.long_to_short_map[longUrl] = short_code

        return base_url + self.long_to_short_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """
        Decodes a shortened URL back to its original long URL.
        """
        # Extract the last 6 characters as the short code
        short_code = shortUrl[-6:]
        return self.short_to_long_map.get(short_code, "")

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))