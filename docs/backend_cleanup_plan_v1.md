# Backend Folder Cleanup Plan (v1.0)

## Objective
Clean up the `backend-django` directory in the starter kit to contain *only* the `initial_data.sql` file. This involves replacing the existing contents with the updated `initial_data.sql` currently located in the project root.

## Scope
- **Repository**: `globalbooks_Vue3-Django_starter`
- **Target Directory**: `backend-django`

## Steps
1. **Clean Target Directory**:
   - Delete all files and subdirectories within `backend-django` (`manage.py`, `myproject/`, `requirements.txt`, `run_django.bat`, and existing `initial_data.sql`).
2. **Move File**:
   - Move `initial_data.sql` from the project root to `backend-django/`.
3. **Documentation**:
   - Save this plan to `docs/backend_cleanup_plan_v1.md`.
4. **Commit & Push**:
   - Commit the deletion, move, and documentation.
   - Push to `origin/starter`.

## Verification
- Verify `backend-django` contains only `initial_data.sql`.
- Verify project root no longer contains `initial_data.sql`.
