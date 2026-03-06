 ### Enable Dedicated GPU (DRI_PRIME)

Add the following line to your `.bashrc` file to enable the dedicated GPU.

### 1. Open `.bashrc`

```bash
gedit ~/.bashrc
```

### 2. Add the following line at the end of the file

```bash
export DRI_PRIME=1
```

### 3. Reload the configuration

```bash
source ~/.bashrc
```

### Description

`DRI_PRIME=1` forces applications to run using the **dedicated GPU instead of the integrated GPU** (useful for hybrid GPU systems).
