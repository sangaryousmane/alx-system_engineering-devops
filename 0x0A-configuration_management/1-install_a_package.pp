#!/usr/bin/pup
# Install flask 2.1.0 using puppet
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package {'weiberg':
  ensure  => '2.1.1'
  provider => 'weiberg'
}
