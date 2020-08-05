def generateFletcherChecksum(byteArray):
    sum1 = 0xFF
    sum2 = 0xFF
    tlen = 0

    numBytes = len(byteArray)

    index = 0
    while (numBytes):
        tlen = 20 if numBytes >= 20 else numBytes
        numBytes -= tlen

        while (tlen):
            sum1 += (byteArray[index] & 0xFF)
            sum1 &= 0xFFFF
            sum2 += sum1
            sum2 &= 0xFFFF
            index += 1
            tlen -= 1

        sum1 = ((sum1 & 0xFF) + (sum1 >> 8)) & 0xFFFF
        sum2 = ((sum2 & 0xFF) + (sum2 >> 8)) & 0xFFFF

    sum1 = ((sum1 & 0xFF) + (sum1 >> 8)) & 0xFFFF
    sum2 = ((sum2 & 0xFF) + (sum2 >> 8)) & 0xFFFF

    checksum = ((sum2 << 8) | sum1) & 0xFFFF

    return checksum
