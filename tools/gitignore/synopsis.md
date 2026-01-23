# .gitignore

*from Documentation*


## References

[Source](https://git-scm.com/docs/gitignore)

[How to Use a .gitignore File](https://www.pluralsight.com/guides/how-to-use-gitignore-file)


## Pattern Format

A `.gitignore` file specifies intentionally untracked files that Git should ignore. Files already tracked by Git are not affected.

`#` - comment line.

`!` - (negate pattern) include again.

`/` - directory separator.

`*` - any characters, except `/`.

`?` - any one character, except `/`.

`[a-zA-Z]` - one character in a range.

If there is a separator at the beginning or middle (or both) of the pattern, then the pattern is relative to the directory level of the particular `.gitignore` file itself. Otherwise the pattern may also match at any level below the `.gitignore` level.

If there is a separator at the end of the pattern then the pattern will only match directories, otherwise the pattern can match both files and directories.

For example, a pattern `doc/frotz/` matches `doc/frotz` directory, but not `a/doc/frotz` directory; however `frotz/` matches `frotz` and `a/frotz` that is a directory (all paths are relative from the `.gitignore` file).

A leading `**` followed by a slash means match in all directories. For example, `**/foo` matches file or directory `foo` anywhere, the same as pattern `foo`. `**/foo/bar` matches file or directory `bar` anywhere that is directly under directory `foo`.

A trailing `/**` matches everything inside. For example, `abc/**` matches all files inside directory `abc`, relative to the location of the `.gitignore` file, with infinite depth.

A slash followed by two consecutive asterisks then a slash matches zero or more directories. For example, `a/**/b` matches `a/b`, `a/x/b`, `a/x/y/b` and so on.


## Undo a commit

`git reset HEAD~`
