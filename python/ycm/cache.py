class CacheEntry( object ):
    def __init__( self, diagnostics, skipped_ranges ):
        self.diagnostics = diagnostics
        self.skipped_ranges = skipped_ranges


class BufferDataCache( object ):
    def __init__(self):
        self.__cache = {}

    def Store( self, filename, diagnostics, skipped_ranges ):
        self.__cache[ filename ] = CacheEntry( diagnostics, skipped_ranges )

    def Get( self, filename ):
        if self.__cache.has_key( filename ):
            return self.__cache[ filename ]

        return None

    def Clear(self, filename ):
        if self.__cache.has_key( filename ):
            del self.__cache[ filename ]

