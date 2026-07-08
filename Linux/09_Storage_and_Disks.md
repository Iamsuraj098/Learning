#  09_Storage_and_Disks

### 1. How Linux Sees Storage ?

In linux everything treated as the a file.

Hard disks, SSDs, USB drives, DVDs—all appear as device files under:

Bash: `/dev`

Example: `ls /dev`

We may see: 
```
sda
sda1
sda2
nvme0n1
nvme0n1p1
loop0
tty
```
We can think like this - 
```
Computer
    │
    ├── SSD
    │      │
    │      ├── Partition 1
    │      ├── Partition 2
    │
    └── USB
           │
           └── Partition 1
```
 
---

### 2. Disk Name Convention

Different storage types have different name.

| Device           | Meaning                |
| ---------------- | ---------------------- |
| `/dev/sda`       | First SATA/SCSI disk   |
| `/dev/sdb`       | Second SATA/SCSI disk  |
| `/dev/sdc`       | Third disk             |
| `/dev/sda1`      | First partition on sda |
| `/dev/sda2`      | Second partition       |
| `/dev/nvme0n1`   | First NVMe SSD         |
| `/dev/nvme0n1p1` | First NVMe partition   |
| `/dev/loop0`     | Loop device            |
| `/dev/sr0`       | CD/DVD drive           |

---

### 3. View All Storage device

lsblk
Most commonly used command.
Syntax: `lsblk`

Example:
```
NAME   SIZE TYPE MOUNTPOINT
sda    100G disk
├─sda1 512M part /boot
├─sda2  50G part /
└─sda3  49G part /home
```

| Column     | Description        |
| ---------- | ------------------ |
| NAME       | Device name        |
| SIZE       | Capacity           |
| TYPE       | Disk or partition  |
| MOUNTPOINT | Where it's mounted |


---

### 4. Check Device Usage `df`

Show file system Usage
Syntax: `df`
Better Syntax: `df -h`

Example:
```
Filesystem Size Used Avail Use%
/dev/sda2 50G 20G 28G 42%
```

Abbreviation:

| Column     | Description    |
| ---------- | -------------- |
| Size       | Total size     |
| Used       | Used space     |
| Avail      | Free space     |
| Use%       | Utilization    |
| Mounted on | Mount location |

---

### Check Folder Size

Unlike `df`, which reports filesystem usage, `du` reports the size of files and directories.

Syntax: `df`

Human Readable: `df -h`

Current directory summary: `du -sh .`

Widerly Use command:

| Command    | Description                                |
| ---------- | ------------------------------------------ |
| `du -h`    | Human-readable sizes                       |
| `du -sh`   | Total size of current directory            |
| `du -sh *` | Size of each item in the current directory |


---

### 6. Filesystem vs Partation

#### Partition

A partition is a logical section of a disk.

Example:
```
500 GB SSD

-------------------------
|100G|200G|200G|
-------------------------

Partition1
Partition2
Partition3
```

#### Filesystem

A filesystem defines how data is organized and stored within a partition.

Examples:

```
Partition
↓
Format it
↓
ext4
↓
Ready to store files
```

Without a filesystem, a partition cannot be used to store files in a meaningful way.

---

### 7. Common Linux Filesystems
| Filesystem | Description                                                            |
| ---------- | ---------------------------------------------------------------------- |
| ext4       | Default and most widely used Linux filesystem                          |
| XFS        | Optimized for very large files and filesystems                         |
| Btrfs      | Advanced filesystem with snapshots and checksums                       |
| FAT32      | Compatible with almost all operating systems, but has file size limits |
| exFAT      | Better cross-platform support for large files, common on USB drives    |
| NTFS       | Native filesystem used by Windows                                      |

---
---

# Chapter 09 – Storage and Disks (Part 2)

# 1. Mounting a Filesystem

A partition is not accessible until it is **mounted**.

Linux attaches a filesystem to a directory called a **mount point**.

Example:

```text
Disk
 └── Partition (/dev/sdb1)
          │
          ▼
Mounted at
          │
          ▼
      /mnt/usb
```

Now everything stored in `/dev/sdb1` is accessible through `/mnt/usb`.

---

## View Mounted Filesystems

```bash
mount
```

The output can be long, so a better option is:

```bash
mount | less
```

Or use:

```bash
findmnts
```

Example:

```text
TARGET    SOURCE      FSTYPE
/         /dev/sda2   ext4
/boot     /dev/sda1   ext4
```

---

## Mount a Device

Create a mount point:

```bash
sudo mkdir /mnt/usb
```

Mount the partition:

```bash
sudo mount /dev/sdb1 /mnt/usb
```

Verify:

```bash
df -h
```

or

```bash
findmnt
```

---

# 2. Unmounting

Before removing a USB drive, unmount it to avoid data corruption.

```bash
sudo umount /mnt/usb
```

or

```bash
sudo umount /dev/sdb1
```

Note:

The command is `umount`, **not** `unmount`.

---

## "Target is busy" Error

Example:

```text
umount: target is busy
```

Common causes:

* A terminal is open inside the mounted directory.
* A file is currently being used.

Find the processes:

```bash
lsof /mnt/usb
```

or

```bash
fuser -vm /mnt/usb
```

---

# 3. Automatic Mounting with `/etc/fstab`

Normally, manually mounted filesystems disappear after a reboot.

Linux uses:

```bash
/etc/fstab
```

to mount filesystems automatically during boot.

Example:

```text
UUID=abcd1234  /data  ext4  defaults  0  2
```

Fields:

| Field       | Meaning                            |
| ----------- | ---------------------------------- |
| UUID        | Filesystem identifier              |
| Mount Point | Directory where it is mounted      |
| Filesystem  | ext4, xfs, etc.                    |
| Options     | Mount options                      |
| Dump        | Backup option (usually `0`)        |
| Pass        | Filesystem check order during boot |

---

## Find a UUID

```bash
lsblk -f
```

or

```bash
sudo blkid
```

---

## Test `fstab`

After editing:

```bash
sudo mount -a
```

If no errors appear, the configuration is likely correct.

---

# 4. Creating a Filesystem

Formatting prepares a partition for storing files.

Example:

```bash
sudo mkfs.ext4 /dev/sdb1
```

Other examples:

```bash
sudo mkfs.xfs /dev/sdb1
```

```bash
sudo mkfs.vfat /dev/sdb1
```

Warning:

Formatting **erases all existing data** on the partition.

---

# 5. Creating Partitions

Linux provides several partitioning tools.

| Tool     | Description                        |
| -------- | ---------------------------------- |
| `fdisk`  | Traditional tool for MBR/GPT disks |
| `parted` | Supports large disks and GPT       |
| `gdisk`  | GPT-focused partition editor       |

---

## View Partition Table

```bash
sudo fdisk -l
```

Example:

```text
Disk /dev/sda: 100 GiB

Device       Start      End
/dev/sda1     2048  1050623
/dev/sda2  1050624 99999999
```

---

## Start Interactive `fdisk`

```bash
sudo fdisk /dev/sdb
```

Useful commands inside `fdisk`:

| Command | Action                |
| ------- | --------------------- |
| `m`     | Help                  |
| `p`     | Print partition table |
| `n`     | New partition         |
| `d`     | Delete partition      |
| `w`     | Write changes         |
| `q`     | Quit without saving   |

---

# 6. Filesystem Check (`fsck`)

Checks and repairs filesystem errors.

Example:

```bash
sudo fsck /dev/sdb1
```

Important:

Never run `fsck` on a mounted filesystem.

Unmount it first:

```bash
sudo umount /dev/sdb1
sudo fsck /dev/sdb1
```

---

# 7. Swap Space

Swap is disk space used as an extension of RAM when memory becomes full.

```text
RAM Full
    │
    ▼
Swap Space
```

Swap is slower than RAM but helps prevent crashes due to memory exhaustion.

---

## Check Swap

```bash
swapon --show
```

or

```bash
free -h
```

Example:

```text
Swap: 2.0G
```

---

# 8. LVM (Logical Volume Manager)

LVM provides flexible storage management.

Traditional layout:

```text
Disk
 ├── Partition 1
 ├── Partition 2
```

LVM layout:

```text
Disk
   │
Physical Volume (PV)
   │
Volume Group (VG)
   │
Logical Volumes (LV)
```

Benefits:

* Resize storage easily.
* Combine multiple disks.
* Extend partitions without repartitioning the disk.
* Easier storage management.

Basic commands:

```bash
pvcreate
vgcreate
lvcreate
lvextend
lvremove
```

---

# 9. Useful Storage Commands

| Command         | Description                      |
| --------------- | -------------------------------- |
| `lsblk`         | Show disks and partitions        |
| `lsblk -f`      | Show filesystems and UUIDs       |
| `df -h`         | Filesystem usage                 |
| `du -sh`        | Directory size                   |
| `mount`         | Display mounted filesystems      |
| `findmnt`       | Tree view of mounted filesystems |
| `umount`        | Unmount a filesystem             |
| `blkid`         | Display UUID information         |
| `mkfs.ext4`     | Create an ext4 filesystem        |
| `fdisk -l`      | List partition tables            |
| `fsck`          | Check and repair filesystems     |
| `free -h`       | Display RAM and swap usage       |
| `swapon --show` | Display active swap              |

---

# Practical Lab

Run the following commands on your Ubuntu system:

```bash
lsblk

lsblk -f

findmnt

df -h

du -sh ~

sudo fdisk -l

sudo blkid

free -h

swapon --show
```

Try to identify:

* Your physical disks.
* All partitions.
* Which partition is mounted as `/`.
* Filesystem types.
* UUIDs.
* Total and available disk space.
* Whether swap is enabled.

Do **not** run these commands on your main system unless you understand the consequences:

```bash
sudo mkfs.ext4 /dev/sdb1
sudo fdisk /dev/sdb
sudo fsck /dev/sda1
```

These commands can modify or erase disk data.





















































