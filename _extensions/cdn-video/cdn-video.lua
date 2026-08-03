-- cdn-video shortcode
--
-- Emits a native HTML5 <video> element for a video hosted on cdn.posit.co.
--
--   {{< cdn-video https://cdn.posit.co/positron/releases/videos/plots.mp4
--      poster="https://cdn.posit.co/positron/releases/videos/plots-poster.jpg"
--      aria-label="Video demonstration of the Plots Pane" >}}
--
-- Both URLs are written out in full on purpose. What you read in the .qmd is
-- exactly what the browser requests, so the URLs are greppable and there is no
-- hidden rewriting between source and output.
--
-- This deliberately does NOT use Quarto's built-in {{< video >}} shortcode.
-- That one calls quarto.doc.add_html_dependency() unconditionally for any
-- non-YouTube/Vimeo source (see video.lua:265 in the Quarto install), pulling
-- video.js into <head>: 569 KB of render-blocking JavaScript plus 45 KB of CSS,
-- to power a player we use none of. There is no opt-out, and because the
-- dependency goes into the template rather than the document AST, a filter
-- cannot remove it afterwards. See videos/README.md.

local function meta_string(meta, key, default)
  if meta[key] ~= nil then
    return pandoc.utils.stringify(meta[key])
  end
  return default
end

local function kwarg_string(kwargs, key)
  local v = kwargs[key]
  if v == nil then return nil end
  local s = pandoc.utils.stringify(v)
  if s == "" then return nil end
  return s
end

-- Minimal HTML attribute escaping for values we interpolate into the tag.
-- Tolerates nil so that a validation failure below surfaces its own message
-- rather than a confusing secondary "attempt to index a nil value" trace.
local function esc(s)
  if s == nil then return "" end
  return s:gsub("&", "&amp;"):gsub('"', "&quot;"):gsub("<", "&lt;"):gsub(">", "&gt;")
end

-- Quarto catches a plain error() from a shortcode, logs it, and carries on with
-- exit code 0, which would let a page ship a broken player through CI. The
-- error() call gives the nicely formatted "ERROR (file:line)" message; the
-- os.exit(1) is what actually fails the build and suppresses the output file.
local function fail(msg)
  error(msg)
  os.exit(1)
end

-- Returned as a table with a quoted key because a Lua identifier cannot contain
-- a hyphen, and we want the shortcode to read as {{< cdn-video >}}.
return {
  ["cdn-video"] = function(args, kwargs, meta)
    -- Workbench bundles ship without videos.
    if meta_string(meta, "show-videos", "true") ~= "true" then
      return pandoc.Null()
    end

    if args[1] == nil then
      fail("cdn-video: missing the video URL (first argument)")
    end
    local src = pandoc.utils.stringify(args[1])

    local poster = kwarg_string(kwargs, "poster")
    if poster == nil then
      fail("cdn-video: missing required poster=\"...\" for " .. src ..
           "\nWithout a poster the player renders a black rectangle." ..
           "\nRun `bash videos/generate-posters.sh` and use the matching -poster.jpg URL.")
    end

    local label = kwarg_string(kwargs, "aria-label")
    if label == nil then
      fail("cdn-video: missing required aria-label=\"...\" for " .. src ..
           "\nIt is the only description a screen reader gets.")
    end

    -- Single knob for all videos, set in _quarto-positron.yml.
    local preload = meta_string(meta, "video-preload", "none")

    -- No width/height attributes: sizing is CSS's job (see the VIDEOS section
    -- of css/theme.scss). The HTML width attribute only accepts integer pixels,
    -- so width="100%" would be invalid and silently ignored.
    return pandoc.RawBlock("html", table.concat({
      '<div class="quarto-video">',
      '<video controls playsinline',
      ' preload="', esc(preload), '"',
      ' poster="', esc(poster), '"',
      ' aria-label="', esc(label), '">',
      '<source src="', esc(src), '" type="video/mp4">',
      '</video>',
      '</div>',
    }))
  end
}
