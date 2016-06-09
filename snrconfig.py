import shutil
import os


def exists_copy(computer):
    default_config = '\\\\server\\folder\\IRIS Software\\SnR\\RFID Config - Prod\\' \
                     'IrisSoftware.SNR.Client.UI.Shell.exe.config'
    snrinstall_config = '\\\\{}\\c$\\SnR Install\\RFID Config - Prod\\' \
                'IrisSoftware.SNR.Client.UI.Shell.exe.config'.format(computer)
    final_location = '\\\\{}\\c$\\Program Files (x86)\\Iris Software Inc\\SnR\\' \
                     'IrisSoftware.SNR.Client.UI.Shell.exe.config'.format(computer)
    if os.path.isfile(snrinstall_config):
        shutil.copy(snrinstall_config, final_location)
        print('Copied config to {}'.format(computer))
    elif os.path.isdir('\\\\{}\\c$'.format(computer)):
        shutil.copy(default_config, final_location)
        print('Copied default config to {}'.format(computer))
    else:
        print('Failed to copy to {}'.format(computer))

def main():
    with open('snrtargets.txt', 'r') as f:
        for line in f:
            computer = line.strip('\n')
            exists_copy(computer)

if __name__ == '__main__':
    main()
