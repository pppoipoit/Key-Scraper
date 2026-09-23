# Product Requirements

## Requirement writing rules

- ทุก requirement ต้องมี ID เช่น FR-001
- แยก functional/non-functional requirement
- ระบุ status: Proposed / Approved / Implemented / Deprecated
- ระบุ source: Owner / Existing behavior / Decision / Assumption

## Functional requirements

ตาราง:
| ID | Requirement | User role | Priority | Status | Source | Notes |
|----|-------------|-----------|----------|--------|--------|-------|
| FR-001 | User can input multiple URLs (one per line) | Operator | P1 | Implemented | Existing behavior | App.py url_text widget |
| FR-002 | User can select destination folder for downloaded images | Operator | P1 | Implemented | Existing behavior | path_entry widget |
| FR-003 | App scrapes URLs in parallel (max 4 concurrent) | Operator | P2 | Implemented | Existing behavior | MAX_PARALLEL_URLS = 4 |
| FR-004 | App extracts model names from detail rows (div.detail_row) | System | P1 | Implemented | Existing behavior | process_row function |
| FR-005 | App detects brand from model name prefix | System | P1 | Implemented | Existing behavior | get_brand_name function |
| FR-006 | App downloads images to brand-specific folders by key type | System | P1 | Implemented | Existing behavior | build_brand_folders |
| FR-007 | Folder structure must be exactly: Layout / LARGER KEYS / REGULAR KEY / SMALLER KEYS | System | P1 | Implemented | Existing behavior | FOLDER_LAYOUT constants |
| FR-008 | Brand folder names must match original (Acer, ASUS, MSI, 삼성전자, DELL, HP, Lenovo, TOSHIBA, Apple, Others) | System | P1 | Implemented | Existing behavior | get_brand_name mapping |
| FR-009 | App shows progress bar for parallel scraping | Operator | P3 | Implemented | Existing behavior | GradientProgressBar |
| FR-010 | App logs scraping activity in scrollable log panel | Operator | P3 | Implemented | Existing behavior | log_text widget |
| FR-011 | App validates: URLs present before start, destination folder selected | Operator | P2 | Implemented | Existing behavior | start_download_thread checks |
| FR-012 | User receives success/error notification after scraping completes | Operator | P2 | Implemented | Existing behavior | messagebox dialogs |

## Business rules

ตาราง:
| ID | Rule | Example | Status | Source |
|----|------|---------|--------|--------|
| BR-001 | Model brand determined by first alphabetic prefix of model code | "AC763" → Acer, "GN745" → Others | Must preserve | Existing behavior |
| BR-002 | Download URL images as-is: regular from img[0], larger from img[1], smaller from img[2] | Order matters | Must preserve | Existing behavior |
| BR-003 | Keyboard layout image (div.keyboar_wrap > img) saved to separate "Layout" folder | Landmark image | Must preserve | Existing behavior |
| BR-004 | No deduplication if same model appears in multiple URLs | All downloads kept | Assumption | Existing behavior |
| BR-005 | Empty URL or no destination = block start with warning | UX validation | Implemented | Existing behavior |

## Permissions and roles

ตาราง:
| Role | Can do | Cannot do | Notes |
|------|--------|-----------|-------|
| Operator | Input URLs, select folder, start/stop scraping, view logs/ progress. | No admin/config access | Single role app |

## Non-functional requirements

- **Performance**: Parallel scraping up to 4 URLs; reasonable speed for typical product pages
- **Reliability**: Graceful failure if one URL fails (logs error, continues others); no app crash
- **Accessibility**: Standard tkinter widgets with keyboard navigation support basic accessibility
- **Security**: No data sent to external services beyond target URLs (no telemetry)
- **Privacy**: No user data collected or stored by app
- **Compatibility**: Windows desktop (icon.ico support); Linux/Mac icon fallback
- **Observability**: Log panel shows real-time scraping status

## Out of scope

- User authentication, accounts, databases
- Web-based version
- Image editing/processing beyond download
- Support for sites beyond the specific 4-folder, brand-prefix structure
- Automated scheduler/cron
- Export/import URL lists
- Configuration GUI for MAX_PARALLEL_URLS

## Assumptions

- Target website HTML structure stable
- Brand detection logic (prefix mapping) accurate enough for use case
- Single local user operating the desktop app
- Python + required libraries available (requests, bs4, Pillow)

## Open questions

- Is there a specific target domain(s) the app is meant for? (Currently reads any URL with matching HTML structure)
- Should MAX_PARALLEL_URLS be user-configurable?
- Are there future requirements for additional brand detection rules or site structures?

## Change history

- v2 (current): Parallel multi-URL scraping, gradient UI, progress bar, scrollable logs, brand folder organization preserved