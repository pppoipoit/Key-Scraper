# UI / UX Specification

## Design principles

- **Dark dashboard aesthetic**: Deep navy/indigo background with gradient cards
- **Clear visual hierarchy**: Header with badge → main content cards → action row
- **Feedback-rich**: Progress bar, scrollable log, success/error dialogs
- **Tactile interaction**: Hover effects on buttons, gradient transitions
- **Single-purpose focus**: This is not a multi-feature app; UI reflects one clear workflow

## Visual identity

From `theme.py`:

| Element | Value | Purpose |
|---------|-------|---------|
| Background | `#11132A` (near-black navy) | App background |
| Panel background | `#1A1D3A` | Card interiors |
| Panel light | `#222648` | Inner card backgrounds |
| Border soft | `#30355E` | Subtle dividers |
| Title text | `#F5F6FA` (white-blue) | Main headings |
| Body text | `#C7CBE8` | General text |
| Muted text | `#7E84B3` | Secondary info |
| Font family | Segoe UI | Modern clean sans-serif |
| Log font | Consolas 9px | Monospace for log readability |

### Gradient palette (from theme.py)

| Gradient name | Colors | Used for |
|--------------|--------|----------|
| GRADIENT_SUNSET | `#FACC15` → `#FB7185` (yellow→pink) | 98.5% card |
| GRADIENT_OCEAN | `#60A5FA` → `#2563EB` (blue→deep blue) | 2,481 card |
| GRADIENT_MINT | `#34D399` → `#0E7490` (mint→teal) | 31,124 card, progress bar |
| GRADIENT_BERRY | `#F472B6` → `#9333EA` (pink→purple) | $2,125 card, primary button |

## User flows

### Flow 1: Run extraction (primary flow)

**Flow ID**: F-001

**User role**: Operator

**Trigger**: User clicks "START EXTRACTION" button

**Steps**:
1. User opens app → sees main window with dark dashboard theme
2. User pastes one or more URLs into TARGET URL box (one URL per line)
3. User clicks "SELECT FOLDER" → browser dialog opens → user picks destination
4. User clicks "START EXTRACTION"
5. App validates: URLs present? Folder selected? If not, shows warning
6. App starts background thread, updates UI:
   - Button becomes disabled, text changes to "PROCESSING..."
   - Progress bar shows 0/total URLs
   - Log panel shows "Spying on X website(s) now, wait a second Boss..."
7. For each URL completed: progress bar advances, log shows "Done X → Y models downloaded!"
8. When all done: button re-enabled, final log + messagebox with total models downloaded
9. If no models found: messagebox "Oh? No models found!"

**Success state**: Messagebox shows count of models downloaded, button enabled, log shows completion

**Empty state**: N/A (app starts with empty URL box, user must input)

**Loading state**:
- Progress bar fills proportionally to URLs completed
- Log scrolls with real-time activity
- Button disabled during processing

**Error state**:
- No URLs: warning dialog "No URL? Want me to download from heaven or what?!"
- No folder: warning dialog "Choose destination folder first!"
- Individual URL failure: logged in panel, continues with other URLs
- All URLs fail: "Oh? No models found!" messagebox

**Permission denied state**: N/A (single-user desktop app)

**Mobile/responsive notes**: App is fixed-size 980×600, non-resizable. Desktop-only.

**Accessibility notes**:
- Uses standard tkinter widgets (keyboard navigable)
- No custom accessibility layer
- Color contrast: dark theme with light text generally sufficient

### Flow 2: Select destination folder

**Flow ID**: F-002

**User role**: Operator

**Trigger**: Click "SELECT FOLDER" button

**Steps**:
1. Button click opens tkinter.filedialog.askdirectory()
2. User browses and selects folder
3. Path appears in destination entry box
4. Button label returns to "SELECT FOLDER"

**Success state**: Folder path displayed in entry box

**Error state**: If user cancels dialog, path unchanged

## Screen inventory

| Screen ID | Screen/Page | Purpose | User role | Status |
|-----------|-------------|---------|-----------|--------|
| S-001 | Main window | Primary extraction interface | Operator | Implemented |

**S-001 Main window components:**

| Component | Type | Purpose |
|-----------|------|---------|
| Header badge | GradientPanel (46×46 berry gradient) | Visual branding, app icon area |
| Header title | "LaptopKey Scraper" + "Elite Edition v2" | App identity |
| TARGET URL label | Small bold text | Section header |
| URL text area | Multi-line Text widget with scrollbar | Input URLs (one per line) |
| DESTINATION label | Small bold text | Section header |
| Folder entry | Single-line entry with "SELECT FOLDER" button | Show/select destination |
| PROGRESS section | Label + GradientProgressBar | Visual progress indication |
| LOG section | Label + scrollable Text widget | Real-time activity log |
| START EXTRACTION | GradientButton (large, berry gradient) | Primary action button |

## UI decisions

- **Fixed window size (980×600)**: Prevents layout breakage, simplifies design
- **Non-resizable**: Consistent experience across machines
- **Gradient widgets via PIL**: tkinter lacks native gradient/rounded corner/shadow support
- **Daemon thread for scraping**: Allows app to be closed during processing (thread dies with app)
- **Thread pool max 4**: Prevents overwhelming target server, reasonable parallelism
- **Korean folder names**: Must match original exactly (from scraper_core.py constants)

## Content/copy notes

- Tone is informal/friendly in log messages ("Spying on...", "Boss", "Finish already, Boss!")
- Warning messages are direct ("No URL? Want me to download from heaven or what?!")
- Success message friendly and enthusiastic

## Open UX questions

- Should the app support drag-and-drop URL input?
- Should there be a way to save/reuse URL lists?
- Is the fixed window size appropriate for all users?
- Should progress show percentage in addition to URL count?