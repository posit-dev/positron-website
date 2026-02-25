-- video-filter.lua
-- Removes video elements when show-videos metadata is false
-- This allows using the built-in {{< video >}} shortcode while
-- conditionally excluding videos in certain profiles (e.g., workbench)

local show_videos = true

function Meta(meta)
  -- Check the show-videos metadata value
  if meta["show-videos"] ~= nil then
    show_videos = pandoc.utils.stringify(meta["show-videos"]) == "true"
  end
end

function Div(el)
  -- Remove quarto-video divs when show-videos is false
  if not show_videos and el.classes:includes("quarto-video") then
    return {}
  end
  return el
end

function RawBlock(el)
  -- Remove video HTML blocks when show-videos is false
  if not show_videos and el.format == "html" then
    if el.text:match('<div class="quarto%-video') or
       el.text:match("<video") then
      return {}
    end
  end
  return el
end

-- Return filters in order: Meta first to read settings, then content filters
return {
  { Meta = Meta },
  { Div = Div, RawBlock = RawBlock }
}
