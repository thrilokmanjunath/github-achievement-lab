# GitHub Achievement Guide

> A structured reference for legitimately earning GitHub profile achievements.
> All methods described here comply fully with GitHub's Terms of Service.

---

## Important Disclaimer

> ⚠️ **Do not** use bots, fake accounts, purchased stars, or any deceptive
> method to earn achievements. GitHub monitors for abuse and may remove
> achievements or suspend accounts. Every achievement listed here can only
> be earned through **genuine** GitHub activity.

---

## Achievement Status Key

| Symbol | Meaning |
|---|---|
| 🟢 Available | Currently earnable through normal GitHub activity |
| 🟡 Conditional | Earnable but depends on external factors (e.g., other users) |
| 🔴 Historical | No longer earnable — awarded to those who earned it before the cutoff |

---

## Currently Earnable Achievements

---

### 🟢 Pull Shark

**Requirement**: Merge pull requests into a repository you own or contribute to.

| Tier | Requirement |
|---|---|
| 🥉 Bronze | 2 merged pull requests |
| 🥈 Silver | 16 merged pull requests |
| 🥇 Gold | 128 merged pull requests |

**How to earn it legitimately:**

1. Create a feature branch: `git checkout -b feature/my-feature`
2. Make a real change (add a function, fix a bug, improve docs)
3. Push and open a PR: `gh pr create`
4. Verify CI passes
5. Merge the PR: `gh pr merge --squash`

**Notes:**
- PRs must be merged (not just opened)
- Works on your own public repositories
- Each meaningful feature, fix, or improvement counts
- Multiple tiers reward sustained contribution

---

### 🟢 Quickdraw

**Requirement**: Close an issue or pull request within 5 minutes of opening it.

**How to earn it legitimately:**

1. Open an issue (e.g., a duplicate you just noticed)
2. Realise it's already addressed or is not needed
3. Close it with a reason within 5 minutes

OR:

1. Open a PR
2. Immediately notice a critical mistake (wrong branch, etc.)
3. Close the PR and open a corrected one

**Notes:**
- The trigger must be genuine — do not open issues solely to close them immediately
- The 5-minute window is calculated from the time of creation

---

### 🟡 Pair Extraordinaire

**Requirement**: Co-author a merged pull request with another real GitHub user.

| Tier | Requirement |
|---|---|
| 🥉 Bronze | 1 co-authored merged PR |
| 🥈 Silver | 10 co-authored merged PRs |
| 🥇 Gold | 100 co-authored merged PRs |

**How to earn it legitimately:**

1. Collaborate genuinely with another developer on a feature
2. Include the `Co-authored-by:` trailer in the commit message:

```
feat(calculator): add statistics command

Co-authored-by: Jane Smith <jane@example.com>
```

3. Open and merge the PR
4. **Both contributors** earn the achievement

**Notes:**
- The co-author must have a real GitHub account linked to that email
- Never invent a person's identity or impersonate someone
- Pair programming sessions, mob programming, and genuine collaboration all qualify

---

### 🟡 Galaxy Brain

**Requirement**: Have a discussion answer accepted as the official "Answer."

| Tier | Requirement |
|---|---|
| 🥉 Bronze | 8 accepted answers |
| 🥈 Silver | 16 accepted answers |
| 🥇 Gold | 32 accepted answers |

**How to earn it legitimately:**

1. Enable Discussions on your repository (Settings → Discussions)
2. Participate in community discussions with genuinely helpful answers
3. The **original poster** marks your answer as the accepted answer

**Notes:**
- You cannot accept your own answers in your own discussions
- The achievement requires the OP to voluntarily mark your answer — it cannot be forced
- The best way to earn this is to be a genuinely helpful community member

---

### 🟡 Starstruck

**Requirement**: Create a repository that receives genuine stars from other users.

| Tier | Requirement |
|---|---|
| 🥉 Bronze | 16 stars |
| 🥈 Silver | 128 stars |
| 🥇 Gold | 512 stars |
| 💎 Platinum | 4096 stars |

**How to earn it legitimately:**

1. Build something genuinely useful and well-documented
2. Share it authentically:
   - Post in relevant communities (Reddit, Dev.to, Hacker News, Discord servers)
   - Write a blog post or article
   - Present it at meetups or conferences
3. Let the community decide whether to star it

**Notes:**
- Purchased stars, bot stars, and star-for-star rings violate GitHub's ToS
- Genuine stars from real users who find the project useful are the only valid path
- This achievement tests the real-world quality and reach of your work

---

### 🟢 YOLO

**Requirement**: Merge a pull request without requesting or receiving a code review.

**How to earn it legitimately:**

1. Open a PR on your own repository
2. Merge it without adding any reviewers or waiting for an approval
3. GitHub awards the achievement automatically

**Notes:**
- This is legitimate on personal/hobby repos
- **Not recommended** for production or collaborative repositories
- For collaborative projects, always follow the code review process

---

### 🟢 Public Sponsor

**Requirement**: Sponsor an open-source developer or organisation via GitHub Sponsors.

**How to earn it legitimately:**

1. Visit [github.com/sponsors](https://github.com/sponsors)
2. Find a developer or project you genuinely want to support
3. Set up a recurring or one-time sponsorship

**Notes:**
- This is a genuine financial contribution
- The achievement is earned upon making your first public sponsorship

---

## Historical Achievements (No Longer Earnable)

---

### 🔴 Arctic Code Vault Contributor

**Requirement**: Contributed code to a public repository that was included in the
[GitHub Arctic Code Vault](https://archiveprogram.github.com/) snapshot taken on **February 2, 2020**.

**Status**: Not earnable. The snapshot has been taken and stored.

---

### 🔴 Mars 2020 Helicopter Contributor

**Requirement**: Contributed to one of the open-source repositories used by
NASA's Ingenuity helicopter on the Mars 2020 mission, with contributions made
before the mission launch.

**Status**: Not earnable. The mission has launched and contributions are fixed.

---

## Strategy for New Accounts

If you are building your GitHub profile from scratch, focus on:

1. **Start with Pull Shark** — open a real project, make genuine improvements, merge PRs
2. **Aim for Quickdraw** — close duplicate issues quickly when you spot them
3. **Build toward Starstruck** — create genuinely useful tools and share them authentically
4. **Find a collaborator for Pair Extraordinaire** — pair program on a real feature
5. **Participate in Discussions for Galaxy Brain** — answer questions you genuinely know

---

## What Does NOT Count

- Issues or PRs opened and closed on empty/throwaway repositories with no content
- Stars from bot accounts
- Co-authored commits with fake/invented identities
- Accepted answers in discussions you created solely to accept your own answer
- Any activity generated by scripts or bots

---

*Last updated: August 2026*
