import subprocess
import pavilion.system_plugins as system_plugins

class SystemArch( system_plugins.SystemPlugins ):

    def __init__( self ):
        super.__init__( 'sys_arch', 10, False, [ None ] )

    def _get( self, sub_key=None ):
        """Base method for determining the system architecture."""

        if sub_key not in self.sub_keys:
            raise KeyError("Sub-key '{}' not found on sys variable {}.".format(
                           sub_key, self.name))

        self.values[ sub_key ] = subprocess.check_output(['uname', '-i'])

        self.values[ sub_key ] = self.values[ sub_key ].strip().decode('UTF-8')

        return self.values[ sub_key ]
