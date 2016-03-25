from ycm import vimsupport
import vim


def _UpdateSkippedRanges( ranges ):
  vimsupport.ClearSkippedRangesSyntaxMatches()

  for (start, end) in ranges:
    vimsupport.AddSkippedRangeSyntaxMatch(start, end)


class SkippedRangesInterface( object ):
  def __init__( self, user_options ):
    self._user_options = user_options

  def UpdateWithNewSkippedRanges( self, ranges ):
    if self._user_options[ 'enable_skipped_ranges_highlighting' ]:
      _UpdateSkippedRanges( ranges )

